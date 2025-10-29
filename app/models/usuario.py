import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.config.db_config import Base


def uuid_generator():
    """Gera UUID como string para compatibilidade"""
    return str(uuid.uuid4())


class Usuario(Base):
    """
    Model de usuário do sistema
    
    Tabela: tbusuarios
    
    Roles disponíveis:
    - analista: Acesso completo exceto gestão de usuários
    - comercial: Gera previsões (sem editar), adiciona variáveis
    - gestao: Gerencia usuários, vê KPIs gerais, não edita previsões
    """
    __tablename__ = "tbusuarios"

    id_usuario = Column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4,
        comment="ID único do usuário"
    )
    
    nome = Column(
        String(100), 
        nullable=False,
        comment="Nome completo do usuário"
    )
    
    email = Column(
        String(100), 
        unique=True, 
        nullable=False,
        index=True,
        comment="Email único para login"
    )
    
    senha_hash = Column(
        String(255), 
        nullable=False,
        comment="Hash bcrypt da senha"
    )
    
    role = Column(
        String(20), 
        nullable=False,
        comment="Perfil do usuário: analista, comercial, gestao"
    )
    
    ativo = Column(
        Boolean, 
        default=True,
        nullable=False,
        comment="Usuário ativo no sistema"
    )
    
    dt_criacao = Column(
        DateTime, 
        default=datetime.utcnow,
        nullable=False,
        comment="Data de criação do usuário"
    )
    
    dt_ultimo_acesso = Column(
        DateTime,
        nullable=True,
        comment="Último acesso ao sistema"
    )

    def __repr__(self):
        return f"<Usuario(id={self.id_usuario}, email={self.email}, role={self.role}, ativo={self.ativo})>"

    def to_dict(self):
        """Converte o model para dicionário (sem senha)"""
        return {
            "id_usuario": str(self.id_usuario),
            "nome": self.nome,
            "email": self.email,
            "role": self.role,
            "ativo": self.ativo,
            "dt_criacao": self.dt_criacao.isoformat() if self.dt_criacao else None,
            "dt_ultimo_acesso": self.dt_ultimo_acesso.isoformat() if self.dt_ultimo_acesso else None,
        }